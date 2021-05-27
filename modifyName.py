from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog,QDialog
from PyQt5.QtCore import  QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QMovie
from selectFolder import Ui_MainWindow
from addNew import Ui_Dialog
import sys,os
from settings import *
from handleData import HandleData
from shutil import copyfile
import pandas as pd
import json

class RenameThread(QThread):

    rename_signal = pyqtSignal(str)

    def __init__(self,model_name,folder_path,include_type):

        super(RenameThread,self).__init__()
        self.hand_data = HandleData()
        self.model_name  = model_name
        self.folder_path = folder_path
        self.include_type = include_type


    def run(self):
        self.rename_files()

    def copy_files(self):

        model_folder_path = os.path.join(self.folder_path, self.model_name+'_Rename')
        if not os.path.exists(model_folder_path):
            os.mkdir(model_folder_path)
        for file in os.listdir(self.folder_path):
            try:
                copyfile(os.path.join(self.folder_path,file),os.path.join(model_folder_path,file))
            except Exception as err:
                # self.rename_signal.emit(fr"<font color=red>{err}</font>")
                continue

        return model_folder_path


    def extend_file_name(self,files):

        for i, old_name in enumerate(files):
            if 'CCC' in old_name and old_name.split('.')[0].endswith('M'):
                new_name = old_name.replace('M', ' EMC')
            elif 'CCC' in old_name and old_name.split('.')[0].endswith('T'):
                new_name = old_name.replace('T', ' Telecommunication')
            elif 'CCC' in old_name and old_name.split('.')[0].endswith('S'):
                new_name = old_name.replace('S', ' safety')
            elif not'FCC' in old_name and 'SAR' in old_name:
                new_name = old_name.replace('US', ' USA')
            elif '55032' in old_name and 'EMC' in old_name:
                new_name = old_name.replace('EMC', '')
            else:
                new_name = old_name
            os.rename(old_name, new_name)


    def rename_files(self):
        current_folder = os.getcwd()
        df = self.hand_data.combine_col(self.include_type)
        df['n_keyword'] = df['Keyword'].apply(lambda i: str(i).strip())
        keywords = df['n_keyword']
        model_folder_path = self.copy_files()  # copy files
        files = os.listdir(model_folder_path)
        os.chdir(model_folder_path)
        self.extend_file_name(files)
        files = os.listdir(model_folder_path)
        os.chdir(model_folder_path) # 跳转到此文件夹



        for i, old_name in enumerate(files):
            # file_name = old_name.lower().replace(['wi-fi','-','_','(',')'],['wifi',' ',' ',' ',' '])
            file_name = old_name.lower().replace('wi-fi', 'wifi').replace('-', ' ').replace('_', ' ').replace('(' ,' ').replace(')',' ')
            # print(i,file_name)
            file_name_split_list = file_name.split('.')[0].split(' ')
            for keyword in keywords:
                words = keyword.replace('-', ' ').lower().split(' ')
                try:
                    # 一个list包含另外一个list?
                    if set(words) <= set(file_name_split_list):
                        new_file_name = (self.model_name.lower() + '-' + df[df['n_keyword'] == keyword]['Combined']).to_list()
                        # print(new_file_name)
                        os.rename(old_name, new_file_name[0] + '.pdf')
                        self.rename_signal.emit('\n')
                        self.rename_signal.emit(f"<font color=blue>{'File '+str(i+1) }</font>")
                        self.rename_signal.emit( old_name)
                        self.rename_signal.emit(f"<font color=red>{'↓'}</font>")
                        self.rename_signal.emit(new_file_name[0]+'.pdf')

                except Exception as error:
                    self.rename_signal.emit(f"<font color=red>{error}</font>")

        os.chdir(current_folder) #跳回原来文件夹


class AddDialog(QDialog,Ui_Dialog):
    def __init__(self):
        super(AddDialog,self).__init__()
        self.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowIcon(QIcon('imgs/add.png'))
        self.btn_save.setStyleSheet(save_btn_style)
        self.setFixedSize(self.width(), self.height())  # 禁止窗体拉伸
        self.btn_save.clicked.connect(self.save_file)

    def save_file(self):
        df = pd.read_excel('Data.xlsx',engine= 'openpyxl')
        keyword = self.line_keyword.text()
        region  = self.line_region.text()
        type = self.line_type.text()
        standard = self.line_standard.text()
        version = self.line_version.text()
        suffix = self.line_suffix.text()
        new_row_text = [keyword,region,type,standard,version,suffix]
        df.loc[df.shape[0]] = new_row_text
        df.to_excel('Data.xlsx',index=False)


class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_UI()


    def init_UI(self):
        self.setStyleSheet('background-color:white')
        self.setWindowIcon(QIcon('imgs/win_icon.png'))
        self.setFixedSize(self.width(), self.height())  # 禁止窗体拉伸
        self.btn_rename.setStyleSheet(rename_btn_style)
        self.text_folder_path.setStyleSheet(folder_path_style)
        self.text_model.setStyleSheet(model_style)
        self.checkBox_type.setStyleSheet(checkbox_style)
        self.btn_rename.clicked.connect(self.rename_files_func)
        self.action_clear_log.triggered.connect(self.clear_log)
        self.action_select_folder.triggered.connect(self.select_folder)
        self.action_keywords.triggered.connect(self.add_new_keywords)
        self.action_save_log.triggered.connect(self.save_log)
        self.init_animation_spinner()
        self.file_path_dict = self.get_file_path()


    def add_new_keywords(self):
        add_dialog = AddDialog()
        add_dialog.exec()

    def save_log(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "desktop")
        with open(os.path.join(desktop_path,'rename_log.text'),'w') as f:
            f.write(self.text_log.toPlainText())


    def clear_log(self):
        self.text_log.clear()


    def set_log(self,log):
        self.text_log.append(log)

    def init_animation_spinner(self):
        self.movie = QMovie(self)
        self.animated_spinner = QMovie('imgs/loading.gif')
        self.animated_spinner.frameChanged.connect(self.update_spinner_animation)

    def update_spinner_animation(self):
        self.btn_rename.setIcon(QIcon(self.animated_spinner.currentPixmap()))

    def start_thread(self):
        self.animated_spinner.start()

    def end_thread(self):
        self.animated_spinner.stop()
        self.btn_rename.setIcon(QIcon(''))

    def rename_files_func(self):
        model_name = self.text_model.text()
        folder_path= self.text_folder_path.text()
        includeType = self.checkBox_type.isChecked()

        if model_name =='' or folder_path =='':
            self.text_log.append(fr"<font color=red>{'You must type model name or select reports folder!' }</font>")
            return

        self.rename_thread = RenameThread(model_name,folder_path,includeType)
        self.rename_thread.started.connect(self.start_thread)
        self.rename_thread.finished.connect(self.end_thread)
        self.rename_thread.rename_signal.connect(self.set_log)
        if not self.rename_thread.isRunning():
            self.rename_thread.start()
            self.text_log.append(f"Model name you typed is <font color=red>{model_name}</font>")

    def save_file_path(self):
        json.dump(self.file_path_dict, open('filePath.json', 'w'))

    def get_file_path(self):
        data = json.load(open('filePath.json'))
        return data

    def select_folder(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(self, "Select files folder",self.get_file_path()['folder_path'])
        if folder_path == '':
            return
        self.text_folder_path.setText(folder_path)
        self.file_path_dict['folder_path'] = os.path.dirname(folder_path)
        self.save_file_path()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    # 'pyinstaller -F -w -i C:\Users\h290602\PycharmProjects\FilesRename\imgs\win_icon.ico modifyName.py'
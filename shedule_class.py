from watchdog.events import FileSystemEventHandler
znach: list = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'л', 'к', 'н', 'м', 'с', 'п', 'р', 'ц', 'ф', 'ч', 'ч', 'щ', 'ш', 'd', 'b', 'm', 'n', 'l', 'k', 'p', 't', 'v', 'z', 'p', 'h']

class FileShedule(FileSystemEventHandler):
    def on_created(self, event):
        file_name: str = event.spc_path.split("\\")
        name: str = file_name[-1].split(".")
        name_second: str = name[0]
        name_second.lower()
        for w in name_second:
            if w in znach:
                print(w.upper())
            else:
                print(w.lower())
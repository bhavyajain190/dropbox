import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "s.1Ay8oh91aGNgBB36zS5DIfCW1mAnc6ob0uumdmxcMkZRm5td9GsZOm77d2khX0-q7_XPUoMEtJaVbNbd5k_A7Ub5-DD35e9QBCp2fA-zE7dHqqyYkgH3zBAqOmzmii3OQzOY7Mas"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  

    
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
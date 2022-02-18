from pytube import YouTube

SAVE_PATH = r"C:\Users\jason\OneDrive\Documents\GitHub\Discord-Music-Bot/"
FILE_NAME = 'ytvid.mp4'

#Downloading
def getvid(link=None):
    LINK = link#'https://www.youtube.com/watch?v=5JqY-6q-RNA'
    if link == None or link == '':
        LINK = 'https://www.youtube.com/watch?v=5JqY-6q-RNA'
    try:
        yt = YouTube(LINK)
        yt.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=SAVE_PATH, filename = FILE_NAME)
    except:
        print('Connection Error')
        return False

    print('Download Complete')
    return True


def main():
    link = input('Whats your link: ')
    getvid(link)

if __name__ == '__main__':
    main()

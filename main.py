from win10toast_click import ToastNotifier
from InquirerPy import inquirer
from src.LmsManager import *
import configparser
import webbrowser
import schedule
import time
import sys
import os

config = configparser.ConfigParser()
toaster = ToastNotifier()

if os.path.exists("./Cookie/account_info.ini"):
    pass


else:  # if config.ini not exist
    try:

        username = inquirer.text(message="Username :").execute()
        password = inquirer.secret(message="Password :", transformer=lambda _: "*" * len(username)).execute()
        notif_name = inquirer.select(
            message="Select Notification delay in : ",
            choices=['minute', 'hour'],
        ).execute()

        notif_time = 0
        if notif_name == 'minute':
            notif_time = int(inquirer.text(message="Notif delay in ( Minutes ) :").execute())
        elif notif_name == 'hour':
            notif_time = int(inquirer.text(message="Notif delay in ( Hour ) :").execute())

        lmsm = LmsManager(username=username, password=password)
        lmsm.Login()

        config['account'] = {'username': username, 'password': password}
        config['notif'] = {'time': notif_time, 'type': notif_name}
        with open('./Cookie/account_info.ini', 'w') as configfile:
            config.write(configfile)
        print("Configuration Saved ! ")

        ProfileDetails = lmsm.get_profile()

        toaster.show_toast("Autentikasi Berhasil ✅",
                           "Selamat Datang {full_name}".format(full_name=ProfileDetails['full_name']),
                           icon_path="./icon.ico",
                           duration=5,
                           threaded=True
                           )

    except LoginError as e:
        toaster.show_toast("Oops ada kesalahan ❗️",
                           "Kata sandi atau username salah !\nSilahkan muat ulang program ini",
                           icon_path="./icon.ico",
                           duration=5,
                           threaded=True
                           )
        sys.exit()


def ToastMessage():
    try:

        config.read("config.ini")
        config.read('./Cookie/account_info.ini')
        username = config['account']['username']
        password = config['account']['password']

        try:

            lmsm = LmsManager(username=username, password=password)
            lmsm.Login()

            itteration = 1

            if len(lmsm.Get_activity(end_time=30)) < 1:
                toaster.show_toast("Tidak ada tugas 🙌",
                                   "Semua tugas telah diselesaikan ✅",
                                   icon_path="./icon.ico",
                                   duration=5,
                                   threaded=True)
                return

            for activity in lmsm.Get_activity(end_time=30):

                def open_url(id=activity['id']):
                    try:
                        webbrowser.open_new("https://lms.ittelkom-pwt.ac.id/mod/assign/view.php?id={id}".format(id=id))
                    except:
                        pass

                toaster.show_toast("Tugas ke " + str(itteration),
                                   "📚 Pelajaran : {nama_pelajaran}".format(nama_pelajaran=activity['full_name']),
                                   icon_path="./icon.ico",
                                   duration=7,
                                   )

                toaster.show_toast("Tugas ke " + str(itteration),
                                   "📝 Task Name : {nama_tugas}".format(nama_tugas=activity['name']),
                                   icon_path="./icon.ico",
                                   duration=5,
                                   )

                toaster.show_toast("Tugas ke " + str(itteration),
                                   "🗓 Deadline : {deadline}".format(deadline=activity['deadline']),
                                   icon_path="./icon.ico",
                                   duration=5,
                                   )

                toaster.show_toast("Tugas ke " + str(itteration),
                    "🔗 Klik untuk membuka tugas di LMS",
                    icon_path="./icon.ico",
                    duration=5,
                    threaded=True,
                    callback_on_click=open_url
                )

                itteration += 1
            else:

                toaster.show_toast("Informasi 🙌",
                                   "Jangan lupa mengerjakan tugas yaa ✅",
                                   icon_path="./icon.ico",
                                   duration=5,
                                   threaded=True)



        except LoginError:
            toaster.show_toast("Oops ada kesalahan ❗️",
                               "Kata sandi atau username salah !\nSilahkan muat ulang program ini",
                               icon_path="./icon.ico",
                               duration=5,
                               threaded=True
                               )
            os.remove("./Cookie/account_info.ini")
            sys.exit()

        except GetActivityError:
            toaster.show_toast("Oops ada kesalahan ❗️",
                               "Coba lagi nanti !",
                               icon_path="./icon.ico",
                               duration=5,
                               threaded=True
                               )

        except CookieExpire:
            toaster.show_toast("Oops ada kesalahan ❗️",
                               "Kata sandi atau username salah !\nSilahkan muat ulang program ini",
                               icon_path="./icon.ico",
                               duration=5,
                               threaded=True
                               )

            os.remove("./Cookie/account_info.ini")
            sys.exit()
    except Exception:
        toaster.show_toast("Oops ada kesalahan ❗️",
                           "Coba lagi nanti !",
                           icon_path="./icon.ico",
                           duration=5,
                           threaded=True
                           )
        sys.exit()


try:
    print("Program Running...", flush=True)
    import win32gui
    import win32con

    frgrnd_wndw = win32gui.GetForegroundWindow()
    wndw_title = win32gui.GetWindowText(frgrnd_wndw)
    if wndw_title.endswith("lmsNotifier.exe"):
        win32gui.ShowWindow(frgrnd_wndw, win32con.SW_HIDE)

    config.read("config.ini")
    config.read('./Cookie/account_info.ini')
    username = config['account']['username']
    password = config['account']['password']
    notif_time = config['notif']['time']
    notif_type = config['notif']['type']

    lmsm = LmsManager(username=username, password=password)
    lmsm.Login()

    ProfileDetails = lmsm.get_profile()

    toaster.show_toast("Informasi 😁",
                       "Bot ini akan mengirimkan notifikasi setiap {time} menit".format(time=notif_time),
                       icon_path="./icon.ico",
                       duration=5,
                       )

    toaster.show_toast("Haloo 🙌",
                       "Selamat Datang {full_name}".format(full_name=ProfileDetails['full_name']),
                       icon_path="./icon.ico",
                       duration=5,
                       threaded=True
                       )

    while toaster.notification_active():
        time.sleep(0.1)

    if notif_type == 'minute':
        schedule.every(int(notif_time)).minutes.do(ToastMessage)
    elif notif_type == 'hour':
        schedule.every(int(notif_time)).hours.do(ToastMessage)
    else:
        sys.exit()

    while True:
        schedule.run_pending()
        time.sleep(0.1)

except LoginError as e:
    toaster.show_toast("Oops ada kesalahan",
                       "Kata sandi atau username salah !\nSilahkan muat ulang program ini",
                       icon_path="./icon.ico",
                       duration=5,
                       threaded=True
                       )
    os.remove("./Cookie/account_info.ini")
    sys.exit()

except GetActivityError as e:
    toaster.show_toast("Oops ada kesalahan ❗️",
                       "Coba lagi nanti !",
                       icon_path="./icon.ico",
                       duration=5,
                       threaded=True
                       )


except CookieExpire as e:
    toaster.show_toast("Oops ada kesalahan ❗️",
                       "Kata sandi atau username salah !\nSilahkan muat ulang program ini",
                       icon_path="./icon.ico",
                       duration=5,
                       threaded=True
                       )

    os.remove("./Cookie/account_info.ini")
    sys.exit()
except KeyboardInterrupt:
    toaster.show_toast("Program dihentikan",
                       "Program dihentikan",
                       icon_path="./icon.ico",
                       duration=2,
                       threaded=True
                       )
    sys.exit()

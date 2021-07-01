import json, os, shutil, requests, time, psutil
import PySimpleGUI as sg
#sets modlist
modlist = [
#--aesthetic mods--
#blockus
"https://media.forgecdn.net/files/3273/758/blockus-2.1.1%2B1.16.5.jar",
#bedspreads
"https://media.forgecdn.net/files/3120/448/bedspreads-fabric-1.3.1-1.16.4.jar",
#dark paintings (it's just more paintings lmao)
"https://media.forgecdn.net/files/3358/159/DarkPaintings-Fabric-1.16.5-3.0.2.jar",

#--optifine like mods--
#lithium
"https://media.forgecdn.net/files/3215/441/lithium-fabric-mc1.16.5-0.6.4.jar",
#phosphor
"https://media.forgecdn.net/files/3294/303/phosphor-fabric-mc1.16.3-0.7.2%2Bbuild.12.jar",
#logical zoom
"https://media.forgecdn.net/files/3175/437/logical_zoom-0.0.8.jar",
#dynamicfps
"https://media.forgecdn.net/files/3302/730/dynamic-fps-2.0.2.jar",
#krypton
"https://media.forgecdn.net/files/3200/819/krypton-0.1.2.jar",
#dynamic lighting
"https://media.forgecdn.net/files/3172/563/lambdynamiclights-fabric-1.3.4%2B1.16.jar",
#lazydfu
"https://media.forgecdn.net/files/3209/972/lazydfu-0.1.2.jar",

#--biome/structure mods--
#better end (if you're reading this, i used configs and datapacks to remove infusions and alloying, i just like the pretty biomes)
"https://media.forgecdn.net/files/3360/847/better-end-0.9.8.5-pre.jar",
#dungeons mod
"https://media.forgecdn.net/files/3304/468/DungeonsModLite-1.16.5-1.0.5.jar",
#mo structures
"https://media.forgecdn.net/files/3355/499/mostructures-1.2.0-1.16.5.jar",
#repurposed structures
"https://media.forgecdn.net/files/3346/616/repurposed_structures-1.16.5-1.11.5-fabric.jar",
#traverse (just a couple more biomes lmao)
"https://media.forgecdn.net/files/3209/771/traverse-3.3.2.jar",

#--mob mods--
#bosses of mass destruction (not as chaotic as it sounds)
"https://media.forgecdn.net/files/3340/790/BOMD-1.1.2-1.16.5.jar",
#earth 2 java
"https://media.forgecdn.net/files/3310/364/Earth2Java-1.7.1%2B1.16.4.jar",
#gentle fawn (they had a passive aggressive message at the bottom of their curseforge page, and i just had to have it lmao)
"https://media.forgecdn.net/files/3225/163/GentleFawn-1.1.4-MC1.16.5-fabric.jar",

#--origins mods--
#origins
"https://media.forgecdn.net/files/3260/684/Origins-1.16.5-0.7.0.jar",
#Cursed Origins
"https://media.forgecdn.net/files/3280/486/CursedOrigins-1.16.5-1.1.4.jar",
#Daemonic
"https://media.forgecdn.net/files/3224/992/daemonic-1.1.1.jar",
#ExtraOrigins
"https://media.forgecdn.net/files/3274/277/extraorigins-1.16.5-11.jar",
#moborigins
"https://media.forgecdn.net/files/3280/517/moborigins-1.4.0.jar",
#origins classes
"https://media.forgecdn.net/files/3185/590/Origins-Classes-1.16.5-1.1.1.jar",
#slimeorigin
"https://media.forgecdn.net/files/3292/896/slimeorigin-3.0.0-1.16.x.jar",
#TooManyOrigins
"https://media.forgecdn.net/files/3290/591/TooManyOrigins-1.16.5-0.1.3.jar",
#wiicustomorigins
"https://media.forgecdn.net/files/3249/260/wiicustomorigins-1.16.5-13.jar",

#--core mods--
#simple voice chat
"https://media.forgecdn.net/files/3362/393/voicechat-1.16.5-1.6.3.jar",
#sbm jukebox (hoppers work with jukeboxes)
"https://media.forgecdn.net/files/3016/951/SBM-Jukebox-1.16.1-1.0.2.jar",
#hypnos (morpheus, sleep voting, for fabric)
"https://media.forgecdn.net/files/3284/961/hypnos-0.1.2.jar",
#fabric api
"https://media.forgecdn.net/files/3358/614/fabric-api-0.36.0%2B1.16.jar",
#pehkui
"https://media.forgecdn.net/files/3274/223/Pehkui-2.0.0%2B21w14a.jar",
#data loader (core to the modpack i guess?)
"https://media.forgecdn.net/files/2989/927/data-loader-2.1.0%2Bmc1.16.1.jar",
#DCWA (removes an annoying message caused by better end)
"https://media.forgecdn.net/files/3346/861/DisableCustomWorldsAdvice-1.3.jar",
#bc lib
"https://media.forgecdn.net/files/3360/134/bclib-0.1.43.jar",
#cardinal components
"https://media.forgecdn.net/files/3312/678/Cardinal-Components-API-2.8.3.jar",
#cloth config
"https://media.forgecdn.net/files/3311/351/cloth-config-4.11.26-fabric.jar",
#kotlin
"https://media.forgecdn.net/files/3330/753/fabric-language-kotlin-1.6.1%2Bkotlin.1.5.10.jar",
#geckolib
"https://media.forgecdn.net/files/3343/383/geckolib-fabric-1.16.5-3.0.40.jar"
]

minecraft_version = "1.16.5"
fabric_version = "0.11.3"
max_ram = int(psutil.virtual_memory().total/1028/1028/1028) #gets system ram (truncated)

modpath = os.getenv('APPDATA')+"/.minecraft/mods"#sets variable to mods folder directory
verpath = os.getenv('APPDATA')+"/.minecraft/versions"#sets variable to version directory
vername = "Oripack-1.0"#sets variable to modpack name
oripath = verpath+"/"+vername#sets variable to modpack version directory
mc = os.getenv('APPDATA')+"/.minecraft" #sets variable to minecraft install directory

#sets variable to version profile json
verjson = "https://meta.fabricmc.net/v2/versions/loader/"+minecraft_version+"/"+fabric_version+"/profile/json"
verjson = requests.get(verjson).json()
verjson["id"] = vername

#error handling
datavalidate = False #stores whether datapack installation was successful

#installs mods from a modlist
def mods():
    global modsvalidate
    #Deletes mods folder
    bupdate("resetting mods folder")
    try:
        shutil.rmtree(modpath)
    except:
        print("mods folder not found or failed to be removed")
    
    #creates new mods folder
    try:
        os.mkdir(modpath)
    except:
        try: #checks if .minecraft folder exists
            os.mkdir(mc)
            shutil.rmtree(mc)
            modsvalidate = False
        except: #assumes minecraft is open
            modsvalidate = "open"
    
    if modsvalidate != "open" and modsvalidate != False:
    #sets modpath as working directory
        os.chdir(modpath)
    #downloads mods from modlist (iterating)
        for i in modlist:
            bupdate("downloading "+i.rsplit('/', 1)[1])
            r = requests.get(i)
            print(i.rsplit('/', 1)[1])
            open(i.rsplit('/', 1)[1], 'wb').write(r.content)

#installs fabric modloader
def fabric(ram):
    #deletes broken installations
    bupdate("checking prior installations")
    try:
        shutil.rmtree(oripath)
    except:
        print(vername+" folder not found or failed to be removed.")
    
    #creates Oripack folder
    bupdate("installing fabric")
    os.mkdir(oripath)

    #sets oripath as working directory
    os.chdir(oripath)

    #creates dummyjar in versions folder
    open(vername+".jar", 'w').close()

    #writes version profile json
    f = open(vername+".json", 'w')
    f.write(str(verjson).replace("'", '"'))
    f.close()

    #sets mc as working directory
    os.chdir(mc)    
    
    #grabs current launcher profiles (so they don't get deleted)
    bupdate("modifying launcher_profiles.json")
    f = open("launcher_profiles.json", 'r')
    y = json.loads(f.read())
    f.close()
    #appends new settings to old launcher profiles
    lpjson = json.loads('{"icon" : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGVSURBVHhe7dwxSgRBEEDR1cjUu5iKd/Fg3kVMPYiJmG6mCAOCzOLC4OxM//dA7GTB4FNUt+gBAAAAAAAAAAAYyNXHy+PndL6I2/unq+nIBVxP34kSQJwA4gQQJ4C4i98CWMep25YJECeAOAHECSBudgl8ez9OJ0ZnAsQJIE4AcQKIE0CcAOIEECeAOAHECSBuyKfgm+fX6fTj+HA3nf629PN7YgLECSBOAHECiNt9AN8L2+8vzmcCxAkgTgBxAojbzUvg0uVu1Je8pUyAOAHECSBOAHECiNvkLWDN59ylt4Nzf9at3kJMgDgBxAkgTgBx+SVwztzCNupTtAkQJ4A4AcQJIM4SuBJLIJskgDgBxAkgTgBxAogTQJwA4gQQJ4A4AcQJIE4AcQKIE0Bc5v8DrGmrv/ufYwLECSBOAHECiBNA3G5uAads8c/I9sQEiBNAnADiBBC3+yVwzn8shntf9k4xAeIEECeAOAHEDbkEcj4TIE4AcQKIE0CcAOIEECeAOAHECSBOAAAAAAAAAAAAADCCw+ELoktsVBJsvRMAAAAASUVORK5CYII=","lastVersionId" : "Oripack-1.0","javaArgs" : "-Xmx'+ram+'G -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M","name" : "Oripack!"}')
    y["profiles"]["Billyp673WasHere"]=lpjson

    #reformats launcher profiles to make them minecraft readable
    out = str(y).replace("'", '"').replace("False", 'false').replace("True", 'true')
    #writes to launcher_profiles.json
    f = open("launcher_profiles.json", 'w')
    f.write(out)
    f.close()

#datapack installation
def datapack():
    global datavalidate
    #Deletes configs folder
    bupdate("clearing configs")
    try:
        shutil.rmtree(mc+"/config")
        print("deleted configs")
    except:
        bupdate("failed to remove config folder")
        print("failed to delete configs")
    #datapack directory and file installation
    try:
        os.mkdir(mc+"/config") #creates new config folder
        os.mkdir(mc+"/config/datapacks") #creates datapack folder
        bupdate("downloading Oripack_Tweaks.zip") #updates window text
        os.chdir(mc+"/config/datapacks") #sets directory to configs folder
        #downloads Oripack_Tweaks
        r = requests.get("https://github.com/billyp673/Oripack/releases/download/1.0/Oripack_Tweaks.zip") 
        open("Oripack_Tweaks.zip", 'wb').write(r.content)
        datavalidate = True #tells the rest of the script that the datapack was installed properly
    except:
        print("datapack error") #error message for debug purposes

def configs():
    bupdate("setting configs") #window text
    
    os.chdir(mc+"/config") #look at configs folder
    
    #creates dungeonsmod configs
    r = requests.get("https://raw.githubusercontent.com/billyp673/Oripack/main/config/dungeonsmod.json") #gets configs
    open("dungeonsmod.json", 'wb').write(r.content) #writes configs
    
    #creates betterend config folder
    os.mkdir(mc+"/config/betterend")
    os.chdir(mc+"/config/betterend")

    #creates betterend configs
    bec = ["blocks","items","recipes"] #declare better end configs
    for i in bec: #loop so i dont have to write this for each config
        r = requests.get("https://raw.githubusercontent.com/billyp673/Oripack/main/config/betterend/"+i+".json") #gets configs
        open(i+".json", 'wb').write(r.content) #writes configs
        
#-------------
#-window code-
#-------------

#updates window text
def bupdate(text):
    window["prog"].update(text)
    window.refresh()

stop = False #variable to determine whether the program has completed its task (for exit button)
modsvalidate = True #variable to determine the state of mods folder

#base64 encoded logos
logo = "iVBORw0KGgoAAAANSUhEUgAAAY4AAABACAYAAAANkZAMAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALSSURBVHhe7dwxctQwFAbgLBUtd6FluAsH4y4MLQehYdKmC/GgYkckMv/Ksrzm+2YyuEjee3LBP7K8e3kAOIHH71+ey+XmPnz66v/KK+/KvwDwTwQHABHbL+AURj6q+t/Vj+rsOACICA4AIoIDgIgzDuAU6jOOn7+eyhVbs+MAICI4AIgIDgAiggOAiOAAICI4AIgIDgAizc9xPL8ol5u7vCiXq0bO0XIPM65xn/dxlDXsNUfSp9bq21P3qJ/jeP/tR7n64+nzx3L1t+R3Z7LjACAiOACICA6ADS2Pm65/zkhwABARHABEBAcAkcuoV/K2rDtqxjWtvmndWWtIzJqx1beue8QZF3vNuWXdWTO2/rbHrNdx03OMo75im7DjACAiOACICA4AIs44Glp907qz1pCYNWOrb133iDMu9ppzy7qzZmz9bY89zzi2+nxGet7R6rvn2YkdBwARwQFARHAAEBl2xrGm1beuew8zrpm1hsSsGVt967o9M4605Zx1rVFG3cu95q/d4xlHrT6nSPo44wDgsAQHABHBAXAQy6Op65+jEhwARAQHABHBAUBkWHAsr/q1lF8brrS7yfJa4VtKeYpyy25SbumrSvlNlJI3KSWmK7fsJqXEJspteVVp96ZSgjtmxwFARHAAEBEcAEQEBwARwQFARHAAEBEcAESa76ePfOd6ed+7XK7qmSPpU2v1rev2zDhSsv6eNSR9esyaca1vUrtnDWv2miPpU2v17am759eqX5v1nVJ7fo16zY4DgIjgACDS3Bb2bGXXJFvSnjl6tr6tvnXdnhlHStbfs4akT49ZM671TWr3rGHNXnMkfWqtvj11Zz2qqo18dDXz8dQ1Ow4AIoIDgIjgACBy8/NEgCM5yhlHrefM4yhnGjU7DgAiggOAiOAAIOKMAziFo55xnJEdBwARwQFARHAAEBEcAEQEBwARwQFARHAAEHh4+A1aulu4AE3uugAAAABJRU5ErkJggg=="
errorlogo = "iVBORw0KGgoAAAANSUhEUgAAAY4AAABACAYAAAANkZAMAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALvSURBVHhe7dxBbtQwFAbgDjdgwXE4CTvOwDE4AztOwmWQEGLLrjTCi5Fpnf7jOM6E75Mqsmjfe8mCX7Yzc3kAOIFf3z4+lsvNvX3/xf+VV96UfwHgVQQHABHLL+AURm5V/e/qrTorDgAiggOAiOAAIOKMAziF+ozj+8/f5YqtWXEAEBEcAEQEBwARwQFARHAAEBEcAEQEBwCR5uc4Hp+Uy81dnpTLVSPnaLmHGdd4zvs4yj3sNUfSp9bq21P3qJ/j+Pzja7n669O7D+XqX8nvzmTFAUBEcAAQERwAG1q2m65/zkhwABARHABEBAcAkcuoV/K2rDtqxjWtvmndWfeQmDVjq29d94gzLvaac8u6s2Zs/W2PWa/jpucYR33FNmHFAUBEcAAQERwARJxxNLT6pnVn3UNi1oytvnXdI8642GvOLevOmrH1tz32POPY6vMZ6XlHq++eZydWHABEBAcAEcEBQGTYGceaVt+67j3MuGbWPSRmzdjqW9ftmXGkLeesa40y6lnuNX/tHs84avU5RdLHGQcAhyU4AIjYqmpIZlwz6x4Ss2Zs9a3r9sw40pZz1rVGGfUs95q/doatqh62qgA4LMEBQERwABAZFhzL/mlL+bXhSrubLHu1LynlKcoju0l5pM8q5TdRSt6klJiuPLKblBKbKI/lWaXdi0oJ7pgVBwARwQFARHAAEBEcAEQEBwARwQFARHAAEGm+nz7ynevlfe9yuapnjqRPrdW3rtsz40jJ/ffcQ9Knx6wZ1/omtXvuYc1ecyR9aq2+PXX3/K6qa7O+t2rP76aqWXEAEBEcAESay8KepeyaZEnaM0fP0rfVt67bM+NIyf333EPSp8esGdf6JrV77mHNXnMkfWqtvj11Z21V1UZuXc3cnrpmxQFARHAAEBEcAERu3k8EOJKjnHHUes48jnKmUbPiACAiOACICA4AIs44gFM46hnHGVlxABARHABEBAcAEcEBQERwABARHABEBAcAgYeHP0FCiF8q+5WJAAAAAElFTkSuQmCC"
base64ico = "iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACbSURBVEhLYxgFo4BUwAilGd4fTvoPZaIAQdt5cDXUAAQtpAZAdjSKhS/e/oDyqA80A5aB7WIC8+gISLaQ4+AZKAuVTSwgyUJyLEAHRFuIzbIf9iZQFvGAKAvRLcPGJ9b3ZCcamAXEWgQDZFsIAqRaBgIUWUgOGJwWEpMaiU2xRPsQn4GkZA+SghSbwaRYBgLDv/AeBaNgsAMGBgA5TDFzaASKwgAAAABJRU5ErkJggg=="
#set icon
sg.set_options(icon=bytes(base64ico, 'utf-8'))
#gui code
window = sg.Window(title="Oripack Installer"+vername.replace("Oripack-"," "), layout=[[sg.Image(data=logo, key="logo")],[sg.Text("ready for installation", justification="center", size=(40, 1), key="prog")],[sg.Text("dedicated ram (GB):", size=(15, 1)),sg.In(size=(5, 1), key="ram")],[sg.Button("OK", size=(40, 1))]], margins=(30, 30), element_justification='c')
#window loop
while True:
    event, values = window.read()
    #ok button
    if event == "OK" and stop == False:
        window["OK"].update(disabled = True) #disables ok button during installation
        
        #attempts to install mods
        try:
            mods()
        except:
            modsvalidate = False

        #attempts to install fabric
        if modsvalidate == True:
            try:
                #ramamount is the inputed dedicated ram
                ramamount = int(values["ram"].lower().replace(" ","").replace("gb","").replace("gigabytes","").replace("gigabyte",""))
                if ramamount <= max_ram and ramamount > 0: #checks if ram amount is valid
                    fabric(str(ramamount))
                else:
                    int("notanint") #force an exception (should have prolly used assert lmao)
            except:
                fabric("2") #defaults to 2gb of ram on an exception
            
            #installs datapack
            datapack()
            #error (datapack error) handling
            if datavalidate == True:
                try:
                    configs()
                    bupdate("Oripack is now installed.") #completion message
                except:
                    bupdate("You need to have launched Minecraft atleast once!") #error message                    
            else:
                window["logo"].update(data=errorlogo) #makes logo blue
                bupdate("There was an error installing the datapack.") #error message



        #error handling
        elif modsvalidate == False:
            window["logo"].update(data=errorlogo) #makes logo blue
            bupdate("You need to have launched Minecraft atleast once!") #error message
        else:
            bupdate("Close Minecraft First!") #error message
            window["logo"].update(data=errorlogo) #makes logo blue

    #exit button / window close logic (breaks window loop)
    elif event == sg.WIN_CLOSED or event == "OK" and stop == True:
        break
    
    #turns OK button to EXIT button upon completion
    window["OK"].update(disabled = False)
    window["OK"].update("exit")
    stop = True
window.close() #pretty self explanatory ngl
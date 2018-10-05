import frida, sys
banner = '''
                                                                                         $$\           
                                                                                          $$ |          
 $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$$\  $$$$$$\   $$$$$$$\ $$\   $$\  $$$$$$\   $$$$$$$ |      $$\ 
$$  _____|$$  __$$\ $$  _$$  _$$\ $$  _____|$$  __$$\ $$  _____|$$ |  $$ |$$  __$$\ $$  __$$ |      \__|
$$ /      $$ /  $$ |$$ / $$ / $$ |\$$$$$$\  $$$$$$$$ |$$ /      $$ |  $$ |$$ /  $$ |$$ /  $$ |      $$\ 
$$ |      $$ |  $$ |$$ | $$ | $$ | \____$$\ $$   ____|$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |
\$$$$$$$\ \$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ \$$$$$$$\ \$$$$$$  |\$$$$$$  |\$$$$$$$ |      $$ |
 \_______| \______/ \__| \__| \__|\_______/  \_______| \_______| \______/  \______/  \_______|      $$ |
                                                                                              $$\   $$ |
                                                                                              \$$$$$$  |
                                                                                               \______/ 

     '''
print(banner)

pacage_name = "com.djoh.memory";

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """


Java.perform(function () {

    var Activity = Java.use("java.io.File");
    Activity.$init.overload("java.lang.String").implementation  = function (v1) {
        console.log("v1: " + v1);
    
    Java.perform(function() {
    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))});        
        return this.$init(v1); 

    };

});
"""
 
process = frida.get_usb_device().attach(pacage_name)
script = process.create_script(jscode)
script.on('message', on_message)
print('[+] Frida Attached!')
script.load()
sys.stdin.read()




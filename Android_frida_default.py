import frida, sys
from colorama import Fore, Back, Style, init
init(autoreset=True)
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
                                                                                    
                                                                     Author : djoh(comsecuodj@gmail.com)
     '''
print(Fore.BLUE + banner)

pacage_name = "com.djoh.memory";

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """




Java.perform(function () {


console.log('[+] Hooking Start!');
console.log("");



    var MainActivity = Java.use('com.djoh.memory.MainActivity');
    var RobertTest = Java.use('com.djoh.memory.test1');

      RobertTest.aa.overload().implementation = function () {
        console.log("");
        console.log("***********aa***********");
        console.log("[+] Method Hooking Start!");
        console.log(Object.getOwnPropertyNames(this.__proto__));
        console.log("this.class : "+ this.class);
        console.log("this.aa : " + this.aa);
        console.log("this.num : " + this.num);
        console.log("this.className : " + this.$className);
        console.log("[+] Method Hooking Finish!");
        console.log("****************************");
        console.log("");
        
    };
    




    MainActivity.showMsg.overload('java.lang.String').implementation = function (str) {
        console.log("");
        console.log("***********showMsg***********");
        console.log("[+] Method Hooking Start!");
        console.log("[-] " + str);
        console.log("[+] Method Hooking Finish!");
        console.log("****************************");
        console.log("");
        
    };


    MainActivity.fridatest.implementation = function (a,b) {
        console.log("");
        console.log("***********fridatest***********");
        console.log("[+] Method Hooking Start!");
        console.log("[-] Input param a : " + a +", Input param b :" + b);
        retval = this.fridatest(111111, 200);
        console.log("[-] Hooking Return Value : " + retval);
        return retval;    
        console.log("[+] Method Hooking Finish!");
        console.log("****************************");
        console.log("");
        
    };

    Interceptor.attach(Module.findExportByName("libjniExample.so", 
    "Java_com_djoh_memory_MainActivity_checksu"), { 
        onEnter: function (args) { 
            console.log("***********libjniExample.so***********");
            console.log("[+] Nativelibrary Hooking Start!");
            console.log("[-] Inside native function root_checkfopen"); 
            return 0; 
        }, 
        
        onLeave: function (retval) { 
            retval.replace(0); 
            console.log("[-] inside onleave");
            console.log("[+] Nativelibrary Hooking Finish!");
            console.log("**************************************");
            console.log("");

        } 
    });


});
"""
 
process = frida.get_usb_device().attach(pacage_name)
script = process.create_script(jscode)
script.on('message', on_message)
print(Fore.YELLOW + '[+] Frida Attached!')
script.load()
sys.stdin.read()



'''
    MainActivity.isDebuggable.overload('android.content.Context').implementation = function (str) {
        console.log("***********isDebuggable***********");
        console.log("[+] Method Hooking Start!");
        return false;
        console.log("[+] Method Hooking Finish!");
        console.log("**************************");
        console.log("");
        
    };'''
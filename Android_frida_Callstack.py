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

pacage_name = "test.example.com.ex_dao";

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function() {
        var RobertTest = Java.use('test.example.com.ex_dao.DAO');
		var throwable=Java.use('java.lang.Throwable');

		RobertTest.setName.implementation = function () {
        console.log("");
        console.log("[+] Method Hooking Start!");
		throwable2 = throwable.$new();
		output = throwable2.getStackTrace();
		for ( i=0; i<output.length; i++){
				console.log("[+] ClassName : " + output[i].getClassName()+ ", [+] MethodName : " + output[i].getMethodName());
			}

    };
});
"""
 
process = frida.get_usb_device().attach(pacage_name)
script = process.create_script(jscode)
script.on('message', on_message)
print(Fore.YELLOW + '[+] Frida Attached!')
script.load()
sys.stdin.read()


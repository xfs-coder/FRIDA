rpc.exports = {
    "encrypt": function(str, str2, str3, str4, str5, str6, str7, str8){
                    var result = "";
                    Java.perform(function(){
                        var currentApplication = Java.use("android.app.ActivityThread").currentApplication();
                        var context = currentApplication.getApplicationContext();
                        var UtilEncryptRsa = Java.use("com.ct.client.common.utils.UtilEncryptRsa");
                        result = UtilEncryptRsa.encrypt(context, str, str2, str3, str4, str5, str6, str7, str8);
                    });
                    return result;
               }
}

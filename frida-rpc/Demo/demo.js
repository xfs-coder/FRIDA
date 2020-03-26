rpc.exports = {
    "add": function(a, b){
        var result;
        Java.perform(function(){
            var JNITest = Java.use("com.felix.ndkdemo.JNITest");
            result = JNITest.add(a, b);
        });
        return result;
   }
}
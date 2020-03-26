import frida


def on_message(message, data):
    print(f"[{message}] = > {data}")


def start_hook():
    device = frida.get_usb_device(timeout=5)
    pid = device.spawn(["com.felix.ndkdemo"])
    session = device.attach(pid)
    device.resume(pid)
    
    with open("demo.js", "r", encoding="utf-8") as f:
        jscode = f.read()
    script = session.create_script(jscode)
    script.on('message', on_message)
    script.load()
    return script


if __name__ == '__main__':
    start_hook()
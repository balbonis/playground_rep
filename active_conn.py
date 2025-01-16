from flask import Flask
app = Flask(__name__)

#Sniff Function 
import subprocess
      
def run_netstat():
    try:
        # Start the netstat command
        process = subprocess.Popen(
            ["netstat", "-b", "5"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
       
        # Continuously read and print the output line by line
        global message

        while True:
            output = process.stdout.readline()
            if output:
                print(output.strip())  # Print the output without extra newline
                message = message + "<br>" + output.strip()
            # Break the loop if the process ends
            if process.poll() is not None:
                break

    except KeyboardInterrupt:
        print("\nTerminating the script...")
        process.terminate()  # Terminate the process on user interrupt
    

    except Exception as e:
        print(f"An error occurred: {e}")


#START MAIN
message = "<strong>KABOOM!!!! Sniffing your </strong> " 


@app.route("/")
def home():

    #Timeout settings
    import threading
    import time

    def run_with_timeout (func, timeout):
        def wrapper():
            func()
        thread = threading.Thread(target=wrapper)
        thread.start()
        thread.join(timeout)
        if thread.is_alive():
            print ("End of Process ... Stopping the program")
            return
 
    run_with_timeout(run_netstat,20)  
    return message 
import psutil
import time

def monitor_cpu(threshold=80):
    
    try:
        print("Monitoring CPU usage...")
        while True:
            # Get the current CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Check if CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                print(f"CPU usage is low")
            
            # Sleep for a short duration to prevent overloading the system
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nMonitoring interrupted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    # Set the CPU usage threshold
    cpu_threshold = 80
    
    # Start monitoring
    monitor_cpu(cpu_threshold)
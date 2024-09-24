import subprocess
import sys

def run_docker_container(image_name, container_name, command):
    try:
        # Check if the Docker image exists
        subprocess.run(['docker', 'inspect', '--type=image', image_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print(f"Error: Docker image '{image_name}' does not exist.")
        return

    # Check if a container with the same name is already running
    try:
        result = subprocess.run(['docker', 'inspect', '--type=container', container_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        container_info = result.stdout.decode('utf-8')
        if '"State": {' in container_info:
            print(f"Container with name '{container_name}' is already running.")
            return
        else:
            print(f"Container with name '{container_name}' exists but is not running.")
    except subprocess.CalledProcessError:
        pass

    # Run the Docker container
    try:
        subprocess.run(['docker', 'run', '--name', container_name, '-p', '3000:8080', '-d', image_name, 'bash', 'start.sh'], check=True)
        print(f"Container '{container_name}' started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to start container '{container_name}'.\n{e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python docker.py <image_name> <container_name> <command>")
        sys.exit(1)

    image_name = sys.argv[1]
    container_name = sys.argv[2]
    command = sys.argv[3]

    run_docker_container(image_name, container_name, command)

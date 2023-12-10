def delete_vectorstores():
    """
    Deletes the ./db folder using a subprocess call.
    """
    # Get the absolute path to the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the db folder
    db_folder = os.path.join(script_dir, 'db')

    try:
        # Use the rm command to recursively remove the folder
        subprocess.run(['rm', '-r', db_folder], check=True)
        print(f"The {db_folder} folder has been deleted.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to delete {db_folder}. {e}")

    return jsonify({'status': 'success', 'message': 'Vectorstore deleted successfully'})

def pull_model():
    url = f"{BASE_URL}/api/pull"
    data = {
        "name": model
    }

    response = requests.post(url, json=data)

    # Check the response status
    if response.status_code == 200:
        print("Model pulled.")
    else:
        print(f"Failed to pull model. Status code: {response.status_code}")
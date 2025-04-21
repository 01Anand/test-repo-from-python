import requests
import json
import os
import base64  # Import base64 for encoding file content
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class GitHubAPI:
    # Existing methods...

    def update_file(self, owner, repo, path, new_content, commit_message):
        """
        Updates the content of a file in a GitHub repository.
        :param owner: The owner of the repository.
        :param repo: The name of the repository.
        :param path: The path to the file in the repository.
        :param new_content: The new content to write to the file.
        :param commit_message: The commit message for the update.
        :return: The updated file details.
        """
        # Get the current file details to retrieve the sha
        file_details = self.get_file(owner, repo, path)
        if not file_details:
            print(f"Error: File '{path}' not found in repository '{owner}/{repo}'.")
            return None

        file_sha = file_details["sha"]
        encoded_content = base64.b64encode(new_content.encode()).decode()

        # Prepare the data for the update
        endpoint = f"repos/{owner}/{repo}/contents/{path}"
        data = {
            "message": commit_message,
            "content": encoded_content,
            "sha": file_sha
        }

        # Send the update request
        return self._put(endpoint, data)

new version 
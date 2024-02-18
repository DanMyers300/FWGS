        var chatForm = document.getElementById('chat-form');
        var chatDisplay = document.getElementById('chat-display');
    
        chatForm.addEventListener('submit', function (e) {
            e.preventDefault();
            submitForm();
        });
    
        function submitForm() {
            var queryInput = document.getElementById('query');
            var query = queryInput.value.trim();
    
            if (query !== '') {
                appendMessage('user', query);
                clearQueryBox();
    
                fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ query: query }),
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json()                
                })
                .then(data => {
                    if (data[0] === 'answer') {
                        appendMessage('bot', data[1].answer);
                        if (data[1].documents && data[1].documents.length > 0) {
                            displaySourceDocuments(data[1].documents);
                        }
                    } else {
                        console.error('Error:', data[1].error);
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        }
    
        function displaySourceDocuments(documents) {
            var sourceDocumentsDiv = document.getElementById('source-documents');
            sourceDocumentsDiv.innerHTML = '<h2>Source Documents:</h2>';

            if (documents.length > 0) {
                documents.forEach(document => {
                    var documentDiv = document.createElement('div');
                    documentDiv.innerHTML = '<h3>' + document.metadata.source + '</h3><p>' + document.page_content + '</p>';
                    sourceDocumentsDiv.appendChild(documentDiv);
                });
            } else {
                sourceDocumentsDiv.innerHTML = '<p>No documents available.</p>';
            }
        }

        function clearQueryBox() {
            document.getElementById('query').value = '';
        }
    
        function appendMessage(sender, message) {
            var messageDiv = document.createElement('div');
            messageDiv.className = 'message ' + sender + '-message';
            messageDiv.innerHTML = '<strong>' + sender.charAt(0).toUpperCase() + sender.slice(1) + ':</strong> ' + message;
    
            chatDisplay.appendChild(messageDiv);
            chatDisplay.scrollTop = chatDisplay.scrollHeight;
        }
    
        function toggleCollapsibleBox() {
            var box = document.getElementById('source-documents');
            if (box.style.display === 'none' || box.style.display === '') {
                box.style.display = 'block';
            } else {
                box.style.display = 'none';
            }
        }
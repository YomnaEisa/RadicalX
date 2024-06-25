# pdf_processing.py

# Necessary imports
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import os
import tempfile
import uuid
from tempfile import NamedTemporaryFile

class DocumentProcessor:
    """
    This class encapsulates the functionality for processing uploaded PDF documents using Streamlit
    and Langchain's PyPDFLoader. It provides a method to render a file uploader widget, process the
    uploaded PDF files, extract their pages, and display the total number of pages extracted.
    """
    def __init__(self):
        self.pages = []  # List to keep track of pages from all documents
    
    def ingest_documents(self):
        """
        Renders a file uploader in a Streamlit app, processes uploaded PDF files,
        extracts their pages, and updates the self.pages list with the total number of pages.
        
        Given:
        - Handling of temporary files with unique names to avoid conflicts.
        
        Your Steps:
        1. Utilize the Streamlit file uploader widget to allow users to upload PDF files.
           Hint: Look into st.file_uploader() with the 'type' parameter set to 'pdf'.
        2. For each uploaded PDF file:
           a. Generate a unique identifier and append it to the original file name before saving it temporarily.
              This avoids name conflicts and maintains traceability of the file.
           b. Use Langchain's PyPDFLoader on the path of the temporary file to extract pages.
           c. Clean up by deleting the temporary file after processing.
        3. Keep track of the total number of pages extracted from all uploaded documents.
        
        Example for generating a unique file name with the original name preserved:
        ```
        unique_id = uuid.uuid4().hex
        temp_file_name = f"{original_name}_{unique_id}{file_extension}"
        ```
        """
        
        # Step 1: Render a file uploader widget. Replace 'None' with the Streamlit file uploader code.
            #####################################
            # Allow only type `pdf`
            # Allow multiple PDFs for ingestion
            #####################################
        uploaded_files = st.file_uploader("Upload a PDF File", type=["pdf"], accept_multiple_files=True)
        
        if uploaded_files is not None:
            for uploaded_file in uploaded_files:
                # Generate a unique identifier to append to the file's original name
                unique_id = uuid.uuid4().hex
                original_name = uploaded_file.name
                file_extension = os.path.splitext(original_name)[1]
                
                
                
                with NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
                  temp_file.write(uploaded_file.read())
                  temp_file_name = temp_file.name
                  st.write(f"Temporary file {temp_file_name} created successfully.")             
              

            # Write the uploaded PDF to a temporary file
           # with open(temp_file_path, 'wb') as f:
            #        f.write(uploaded_file.getvalue())


                # Verify the file exists, this was done by them
                if not os.path.exists(temp_file_name):
                    st.error(f"Temporary file {temp_file_name} was not created successfully.")
                    continue
                
                # Debug: Print the file path
                st.write(f"Processing file: {temp_file_name}")
                
                # Use PyPDFLoader to extract pages
                try:
                    loader = PyPDFLoader(temp_file_name)
                    document = loader.load()
                except Exception as e:
                    st.error(f"Failed to load PDF with PyPDFLoader: {e}")
                    continue
                # Step 2: Process the temporary file
                #####################################
                # Use PyPDFLoader here to load the PDF and extract pages.
                # https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#using-pypdf
                # You will need to figure out how to use PyPDFLoader to process the temporary file.
                
                # Use PyPDFLoader to extract pages
                #loader = PyPDFLoader(temp_file_name)
                #document = loader.load()
                # Append the pages to the pages list
                self.pages.extend(document)

    
                # Step 3: Then, Add the extracted pages to the 'pages' list.
                #####################################
               #pages = []
                # Clean up by deleting the temporary file.
                os.unlink(temp_file_name)
            
            # Display the total number of pages processed.
            st.write(f"Total pages processed: {len(self.pages)}")
        
if __name__ == "__main__":
    processor = DocumentProcessor()
    processor.ingest_documents()

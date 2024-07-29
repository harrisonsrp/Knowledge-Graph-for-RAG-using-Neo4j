import json
from langchain.text_splitter import RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 2000,
    chunk_overlap  = 200,
    length_function = len,
    is_separator_regex = False,
)



def split_data_from_file(file):
		#### define a variable to accumlate chunk records
    chunks_with_metadata = [] 
    
    #### Load json file
    file_as_object = json.load(open(file)) 
    keys = list(file_as_object.keys())
    print(keys)
    #### pull these keys from the json file
    for item in keys: 
        print(f'Processing {item} from {file}') 
        
        #### grab the text of the item
        item_text = file_as_object[item] 
        
        #### split the text into chunks
        item_text_chunks = text_splitter.split_text(item_text) 
        
        chunk_seq_id = 0
        #### loop thtough chunks
        for chunk in item_text_chunks: 
        
		        #### extract file name from each chunk
            form_name = file[file.rindex('/') + 1:file.rindex('.')]
            
            #### create a record with metadata and the chunk text
            chunks_with_metadata.append({
                #### metadata from looping...
                'text': chunk, 
                'formItem': item,
                'chunkSeqId': chunk_seq_id,
                #### constructed metadata...
                'chunkId': f'{form_name}-{item}-chunk{chunk_seq_id:04d}',
                'source': file_as_object['Source']
            })
            chunk_seq_id += 1
        print(f'\tSplit into {chunk_seq_id} chunks')
    return chunks_with_metadata
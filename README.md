# Activate virtual env
source streamlit-env/bin/activate

# Run hello_world.py
streamlit run hello_world_sgnc.py --server.enableCORS false --server.enableXsrfProtection false
streamlit run Get_Data_Names.py --server.enableCORS false --server.enableXsrfProtection false
streamlit run cache_demo.py --server.enableCORS false --server.enableXsrfProtection false
streamlit run search_names_by_txtbox.py --server.enableCORS false --server.enableXsrfProtection false
streamlit run segundo.py --server.enableCORS false --server.enableXsrfProtection false
streamlit run tercero.py --server.enableCORS false --server.enableXsrfProtection false
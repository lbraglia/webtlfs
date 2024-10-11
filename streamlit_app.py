from tlfs import TLF
import tempfile
import streamlit as st

# File uploader
xlsx = st.file_uploader(label = "Upload the structure file here, then 'Download TLF'.",
                        type = ["xlsx"],
                        accept_multiple_files = False)

if xlsx is not None:
    struc = tempfile.NamedTemporaryFile(suffix = '.xlsx')
    out = tempfile.NamedTemporaryFile(suffix = '.xlsx')
    strucfile = struc.name
    outfile = out.name
    # salvo per comodità il file in un file
    with open(strucfile, "wb") as f:
        f.write(xlsx.getbuffer())
    tlf = TLF()
    tlf.from_xlsx(strucfile)
    tlf.create(outfile)
    with open(outfile, "rb") as f:
        btn = st.download_button(
            label = "Download TLF",
            data = f,
            file_name = "tlf.xlsx")
    
# Include README
with open('frontpage.md', 'r') as fp:
    frontpage = fp.read()
st.markdown(frontpage)
        

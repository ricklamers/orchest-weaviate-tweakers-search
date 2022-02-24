import orchest
import streamlit as st

from utils import get_weaviate_client

client = get_weaviate_client()

query = st.text_input("Zoek door comments", key="query")

if len(query) > 0:
    content = {
        "concepts": [query],
    }

    result = (
        client.query.get("Comment", ["content", "date"])
        .with_near_text(content)
        .with_limit(10)
        .do()
    )

    comments = result["data"]["Get"]["Comment"]

    if comments is None:
        st.write("Did not find any comments.")
    else:
        for comment in comments:
            st.markdown(comment["date"])
            st.markdown(comment["content"])
            st.markdown("---")

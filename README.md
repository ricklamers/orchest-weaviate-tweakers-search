# Orchest + Weaviate + Tweakers

[![Open in Orchest](https://github.com/orchest/orchest-examples/raw/main/imgs/open_in_orchest.svg)](https://cloud.orchest.io/?import_url=https://github.com/ricklamers/orchest-weaviate-tweakers-search/)

Search for comments using Weaviate's semantic search features.

This pipeline takes a `poster_id` and exposes a Streamlit dashboard to search the comments.

`Fetch Tweakers` takes the following parameters:

```json
{
  "pages": 5,
  "poster_id": "417973"
}
```

<img width="400px" alt="image" src="https://user-images.githubusercontent.com/1309307/155541019-b0672486-b036-46da-9d34-2719b51d91f2.png">


![Pipeline](https://pviz.orchest.io/?pipeline=https://github.com/ricklamers/orchest-weaviate-tweakers-search/blob/master/main.orchest)


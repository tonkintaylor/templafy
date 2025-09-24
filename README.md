# Templafy API Client

A Python client for the Templafy API using openapi-python-client for type-safe, modern Python API access.

## Overview

This package provides a Python client for the Templafy API, generated from the OpenAPI specification.

## Installation

Install the package using uv:

```bash
uv sync
```

Or using pip:

```bash
pip install .
```

## Usage

### Basic Usage

```python
from templafy import Client

# Create a client instance
client = Client(base_url="https://api.templafy.com")

# Make API calls
# Example: Get user information
response = client.get_user(user_id="123")
print(response)
```

### Authenticated Client

For authenticated requests:

```python
from templafy import AuthenticatedClient

# Create an authenticated client
client = AuthenticatedClient(
    base_url="https://api.templafy.com",
    token="your-api-token"
)

# Use the client for authenticated endpoints
response = client.get_secure_data()
```

### Async Usage

The client supports async operations:

```python
import asyncio
from templafy import Client

async def main():
    client = Client(base_url="https://api.templafy.com")
    response = await client.get_user_async(user_id="123")
    print(response)

asyncio.run(main())
```

## API Reference

The client provides methods for all endpoints defined in the OpenAPI specification. Refer to the generated code in `src/templafy/` for detailed method signatures and models.

## Generated Client Structure

```text
src/templafy/
├── client.py           # Base Client and AuthenticatedClient classes
├── errors.py           # Custom exception classes
├── types.py            # Common type definitions
├── api/                # API endpoint implementations
│   ├── __init__.py
│   ├── data_source_fields/  # Data source field endpoints
│   ├── data_source_item_fields/  # Data source item field endpoints
│   ├── data_source_items/   # Data source item endpoints
│   ├── data_sources/        # Data source endpoints
│   ├── documents/           # Document endpoints
│   ├── email_elements/      # Email element endpoints
│   ├── folders/             # Folder endpoints
│   ├── images/              # Image endpoints
│   ├── libraries/           # Library endpoints
│   ├── links/               # Link endpoints
│   ├── pdfs/                # PDF endpoints
│   ├── presentations/       # Presentation endpoints
│   ├── slide_elements/      # Slide element endpoints
│   ├── slides/              # Slide endpoints
│   ├── spaces/              # Space endpoints
│   ├── spreadsheets/        # Spreadsheet endpoints
│   └── text_elements/       # Text element endpoints
└── models/             # Pydantic models for all API schemas
    ├── __init__.py
    ├── space.py        # Space-related models
    ├── library.py      # Library-related models
    ├── document.py     # Document-related models
    ├── folder.py       # Folder-related models
    ├── image.py        # Image-related models
    ├── slide.py        # Slide-related models
    └── ... (additional model files)
```

## Available APIs

| API Group | API Endpoint Name | Description |
|-----------|-------------------|-------------|
| DataSourceFields | get_data_sources_data_source_id_fields_field_id | Gets an existing data source field. |
| DataSourceFields | patch_data_sources_data_source_id_fields_field_id | Updates an existing data source field. |
| DataSourceFields | delete_data_sources_data_source_id_fields_field_id | Deletes a data source field. |
| DataSourceFields | post_data_sources_data_source_id_fields | Creates a new data source field. |
| DataSourceItemFields | put_data_sources_data_source_id_items_item_id_fields_field_id | Updates a single field on a data source item. |
| DataSourceItemFields | delete_data_sources_data_source_id_items_item_id_fields_field_id | Deletes an existing field from a data source item. |
| DataSourceItems | get_data_sources_data_source_id_items | Lists all existing data source items. |
| DataSourceItems | post_data_sources_data_source_id_items | Creates a new data source item. |
| DataSourceItems | get_data_sources_data_source_id_items_item_id | Gets an existing data source item. |
| DataSourceItems | patch_data_sources_data_source_id_items_item_id | Updates data source item. |
| DataSourceItems | delete_data_sources_data_source_id_items_item_id | Deletes an existing data source item. |
| DataSources | get_data_sources | Lists all existing data sources. |
| DataSources | post_data_sources | Creates a new data source. |
| DataSources | get_data_sources_id | Gets an existing data source. |
| DataSources | patch_data_sources_id | Updates an existing data source. |
| DataSources | delete_data_sources_id | Deletes an existing data source. |
| Documents | post_libraries_space_id_documents_assets_asset_id_generate | Generates a document from a template and returns information about the file, which includes the download url. |
| Documents | get_libraries_space_id_documents_folders_folder_id_assets | Lists all document templates in the folder. |
| Documents | post_libraries_space_id_documents_folders_folder_id_assets | Uploads the document template. |
| Documents | get_libraries_space_id_documents_assets_asset_id | Returns the document template by the identifier. |
| Documents | patch_libraries_space_id_documents_assets_asset_id | Updates the document template. |
| Documents | delete_libraries_space_id_documents_assets_asset_id | Deletes the document template by the identifier. |
| EmailElements | get_libraries_space_id_email_elements_folders_folder_id_assets | Lists all email elements in the folder. |
| EmailElements | post_libraries_space_id_email_elements_folders_folder_id_assets | Uploads the email element file. |
| EmailElements | get_libraries_space_id_email_elements_assets_asset_id | Returns the email element by the identifier. |
| EmailElements | patch_libraries_space_id_email_elements_assets_asset_id | Updates the email element asset. |
| EmailElements | delete_libraries_space_id_email_elements_assets_asset_id | Deletes the email element by the identifier. |
| Folders | get_libraries_space_id_library_type_folders_folder_id | Returns the folder by the identifier. |
| Folders | patch_libraries_space_id_library_type_folders_folder_id | Updates the folder. |
| Folders | delete_libraries_space_id_library_type_folders_folder_id | Deletes the folder by the identifier |
| Folders | get_libraries_space_id_library_type_folders_folder_id_folders | Lists all direct folders in the folder. The result does not include subfolders. |
| Folders | post_libraries_space_id_library_type_folders_folder_id_folders | Creates a folder inside the specified folder. |
| Images | get_libraries_space_id_images_folders_folder_id_assets | Lists all image assets in the folder. |
| Images | post_libraries_space_id_images_folders_folder_id_assets | Uploads the image file. |
| Images | get_libraries_space_id_images_assets_asset_id | Returns the image by the identifier. |
| Images | patch_libraries_space_id_images_assets_asset_id | Updates the image asset. |
| Images | delete_libraries_space_id_images_assets_asset_id | Deletes the image by the identifier. |
| Libraries | get_libraries | Lists all libraries from all spaces. |
| Libraries | get_libraries_space_id_library_type | Returns the library by the space identifier and library type. |
| Links | get_libraries_space_id_links_folders_folder_id_assets | Lists all link assets in the folder. |
| Links | post_libraries_space_id_links_folders_folder_id_assets | Creates the link asset. |
| Links | get_libraries_space_id_links_assets_asset_id | Returns the link asset by the identifier. |
| Links | patch_libraries_space_id_links_assets_asset_id | Updates the link asset. |
| Links | delete_libraries_space_id_links_assets_asset_id | Deletes the link by the identifier. |
| Pdfs | get_libraries_space_id_pdfs_folders_folder_id_assets | Lists all pdf assets in the folder. |
| Pdfs | post_libraries_space_id_pdfs_folders_folder_id_assets | Uploads the pdf file. |
| Pdfs | get_libraries_space_id_pdfs_assets_asset_id | Returns the pdf by the identifier. |
| Pdfs | patch_libraries_space_id_pdfs_assets_asset_id | Updates the pdf asset. |
| Pdfs | delete_libraries_space_id_pdfs_assets_asset_id | Deletes the pdf by the identifier. |
| Presentations | post_libraries_space_id_presentations_assets_asset_id_generate | Generates a presentation from a template and returns information about the file, which includes the download url. |
| Presentations | get_libraries_space_id_presentations_folders_folder_id_assets | Lists all presentation templates along with their slides in the folder. |
| Presentations | post_libraries_space_id_presentations_folders_folder_id_assets | Uploads the presentation template. |
| Presentations | get_libraries_space_id_presentations_assets_asset_id | Returns the presentation template or presentation slide by the identifier. |
| Presentations | patch_libraries_space_id_presentations_assets_asset_id | Updates the presentation template. |
| Presentations | delete_libraries_space_id_presentations_assets_asset_id | Deletes the presentation template by the identifier. |
| SlideElements | get_libraries_space_id_slide_elements_folders_folder_id_assets | Lists all slide element decks along with slide elements in the folder. |
| SlideElements | post_libraries_space_id_slide_elements_folders_folder_id_assets | Uploads the slide element file. |
| SlideElements | get_libraries_space_id_slide_elements_assets_asset_id | Returns the slide element deck or slide element by the identifier. |
| SlideElements | patch_libraries_space_id_slide_elements_assets_asset_id | Updates the slide element asset. |
| SlideElements | delete_libraries_space_id_slide_elements_assets_asset_id | Deletes the slide element deck by the identifier. |
| Slides | get_libraries_space_id_slides_folders_folder_id_assets | Lists all slide decks along with slides in the folder. |
| Slides | post_libraries_space_id_slides_folders_folder_id_assets | Uploads the slide file. |
| Slides | get_libraries_space_id_slides_assets_asset_id | Returns the slide deck or slide by the identifier. |
| Slides | patch_libraries_space_id_slides_assets_asset_id | Updates the slide asset. |
| Slides | delete_libraries_space_id_slides_assets_asset_id | Deletes the slide deck by the identifier. |
| Spaces | get_spaces | Lists all existing active spaces. |
| Spreadsheets | post_libraries_space_id_spreadsheets_assets_asset_id_generate | Generates a spreadsheet from a template and returns information about the file, which includes the download url. |
| Spreadsheets | get_libraries_space_id_spreadsheets_folders_folder_id_assets | Lists all spreadsheet templates in the folder. |
| Spreadsheets | post_libraries_space_id_spreadsheets_folders_folder_id_assets | Uploads the spreadsheet template. |
| Spreadsheets | get_libraries_space_id_spreadsheets_assets_asset_id | Returns the spreadsheet template by the identifier. |
| Spreadsheets | patch_libraries_space_id_spreadsheets_assets_asset_id | Updates the spreadsheet template. |
| Spreadsheets | delete_libraries_space_id_spreadsheets_assets_asset_id | Deletes the spreadsheet template by the identifier. |
| TextElements | post_libraries_space_id_text_elements_assets_asset_id_generate | Generates a text element from a template and returns information about the file, which includes the download url. |
| TextElements | get_libraries_space_id_text_elements_folders_folder_id_assets | Lists all text elements in the folder. |
| TextElements | post_libraries_space_id_text_elements_folders_folder_id_assets | Uploads the text element file. |
| TextElements | get_libraries_space_id_text_elements_assets_asset_id | Returns the text element by the identifier. |
| TextElements | patch_libraries_space_id_text_elements_assets_asset_id | Updates the text element asset. |
| TextElements | delete_libraries_space_id_text_elements_assets_asset_id | Deletes the text element by the identifier. |

## Development

This client is generated from `assets/openapi.json` using openapi-python-client. To regenerate:

1. Update the OpenAPI spec in `assets/openapi.json`
2. Run the generation script (see project tasks)

## License

See LICENSE file for details.


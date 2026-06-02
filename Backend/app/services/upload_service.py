import os
import aiofiles

async def save_file(
    collection_id: str,
    file
):
    directory = f"uploads/{collection_id}"

    os.makedirs(
        directory,
        exist_ok=True
    )

    file_path = (
        f"{directory}/{file.filename}"
    )

    async with aiofiles.open(
        file_path,
        "wb"
    ) as out_file:

        content = await file.read()

        await out_file.write(
            content
        )

    return file_path
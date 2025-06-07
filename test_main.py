import os
import shutil
from PIL import Image
from pathlib import Path
from shapes.dataset import generate

def run_generate(output_dir = "test_shapes_dataset", num_train=10, num_val=10, image_size=128, seed=123):
    output_dir = Path(output_dir)
    generate(
        class_names='all',
        num_train=num_train,
        num_val=num_val,
        image_size=image_size,
        output_dir=str(output_dir),
        seed=seed
    )
    return output_dir

def test_generate_creates_output_dir():
    output_dir = run_generate()
    assert output_dir.exists()
    assert output_dir.is_dir()
    shutil.rmtree(output_dir)

def test_generate_creates_expected_folders():
    output_dir = run_generate()
    for split in ['train', 'val']:
        split_dir = output_dir / split
        assert split_dir.exists()
        assert (split_dir / "images").exists()
        assert (split_dir / "masks").exists()
    shutil.rmtree(output_dir)

def test_generate_image_and_mask_dimensions():
    image_size = 80
    output_dir = run_generate(image_size=image_size)
    for split in ['train', 'val']:
        images_dir = output_dir / split / "images"
        masks_dir = output_dir / split / "masks"
        for img_file in os.listdir(images_dir):
            img_path = images_dir / img_file
            with Image.open(img_path) as img:
                assert img.size == (image_size, image_size)
        for mask_file in os.listdir(masks_dir):
            mask_path = masks_dir / mask_file
            with Image.open(mask_path) as mask:
                assert mask.size == (image_size, image_size)
    shutil.rmtree(output_dir)

def test_generate_populates_folders():
    output_dir = run_generate()
    for split in ['train', 'val']:
        images_dir = output_dir / split / "images"
        masks_dir = output_dir / split / "masks"
        assert len(os.listdir(images_dir)) > 0
        assert len(os.listdir(masks_dir)) > 0
    shutil.rmtree(output_dir)
from shapes.dataset import generate

if __name__ == "__main__":
    generate(
        class_names='all',
        num_train=10,
        num_val=10,
        image_size=256,
        output_dir='shapes_dataset',
        seed=42
    )


from transformers import Trainer, TrainingArguments

def train_model(model, train_dataset, test_dataset):

    training_args = TrainingArguments(
        output_dir="results",
        num_train_epochs=3,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset
    )

    trainer.train()

 poetry shell
 mkdir -p saved_models/unix
 mkdir -p saved_models/codebert


 python run.py \
     --output_dir=./saved_models/codebert \
     --tokenizer_name=microsoft/codebert-base \
     --model_name_or_path=microsoft/codebert-base \
     --do_train \
     --train_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/train.jsonl \
     --eval_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/valid.jsonl \
     --test_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/test.jsonl \
     --num_train_epochs 5 \
     --block_size 256 \
     --train_batch_size 8 \
     --eval_batch_size 16 \
     --learning_rate 2e-5 \
     --max_grad_norm 1.0 \
     --seed 123456  2>&1 | tee train-codebert.log
 echo "Finish training codebert"
 echo "training unix"

 python run.py \
     --output_dir=./saved_models/unix \
     --tokenizer_name=microsoft/unixcoder-base \
     --model_name_or_path=microsoft/unixcoder-base \
     --do_train \
     --train_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/train.jsonl \
     --eval_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/valid.jsonl \
     --test_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/test.jsonl \
     --num_train_epochs 5 \
     --block_size 256 \
     --train_batch_size 8 \
     --eval_batch_size 16 \
     --learning_rate 2e-5 \
     --max_grad_norm 1.0 \
     --seed 123456  2>&1 | tee train-unix.log
 echo "Finish training unix"

 # echo "training codet5"
  python run.py \
      --output_dir=./saved_models/codet5 \
      --tokenizer_name=Salesforce/codet5-base \
      --model_name_or_path=Salesforce/codet5-base \
      --do_train \
      --train_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/train.jsonl \
      --eval_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/valid.jsonl \
      --test_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/test.jsonl \
      --num_train_epochs 5 \
      --block_size 256 \
      --train_batch_size 8 \
      --eval_batch_size 16 \
      --learning_rate 2e-5 \
      --max_grad_norm 1.0 \
      --seed 123456  2>&1 | tee train-unix.log

echo "Training distil"

 python run.py \
     --output_dir=./saved_models/distilbert \
     --tokenizer_name=roberta-base \
     --model_name_or_path=roberta-base \
     --do_train \
     --train_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/train.jsonl \
     --eval_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/valid.jsonl \
     --test_data_file=/Users/lfeliped/pipe/master/experiments/jsonl/test.jsonl \
     --num_train_epochs 5 \
     --block_size 256 \
     --train_batch_size 8 \
     --eval_batch_size 16 \
     --learning_rate 2e-5 \
     --max_grad_norm 1.0 \
     --seed 1234

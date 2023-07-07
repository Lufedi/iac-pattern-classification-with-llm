### Description


Implementation code for the project "Fine-tuning LLM pre-trained in code to classify architectural patterns in Infrastructure as code projects"
The goal of the project is fine-tune LLMs in the downstream task of architectural pattern classification. 

### Folder structure
* **steps**:
  * **miner**: python script to mine IaC projects from Github using GitMiner and search expressions
  * **cloner**: python script to clone projects locally
	* **labeler**: python script to add labels from 11 architectural patterns to the cloned files
	* **mapper**: python script transform the labeled data in jsonl format 
	* **trainer**: 
	  * **pattern_categorizer.ipynb**: Playbook to fine-tune LLM using the training dataset built in the previous steps


### Training data
The training data and tuned models are saved in [FigShare](https://figshare.com/articles/dataset/Code_to_arquitecture_pattern_dataset/23537370)

### Paper
In progress


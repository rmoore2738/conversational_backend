from transformers import pipeline

class Generator():
    def __init__(self):
        # Use a smaller, memory-efficient model
        self.model = pipeline('text-generation', model='distilgpt2')

    def generate_options(self, conversation, suggestion_sizes):
        prompts = conversation.get_flat_list()
        suggestions = []
        
        for i, prompt in enumerate(prompts):
            response = self.model(prompt, max_length=30, num_return_sequences=suggestion_sizes[i], do_sample=True)
            options = [r['generated_text'].replace(prompt, '').strip() for r in response]
            suggestions.append(options)

        return suggestions

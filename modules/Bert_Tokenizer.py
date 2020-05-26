from typing import List, Callable
from overrides import overrides
from allennlp.data import Token
from allennlp.data.tokenizers.tokenizer import Tokenizer


@Tokenizer.register("bert")
class Bert_Tokenizer(Tokenizer):

    def __init__(self,
                 tokenizer: Callable[[str], List[str]]):
        self.tokenizer = tokenizer

    @overrides
    def tokenize(self, text: str) -> List[Token]:
        return [Token(text=t) for t in self.tokenizer(text)]

    @overrides
    def batch_tokenize(self, texts: List[str]) -> List[List[Token]]:
        return [self.tokenize(text) for text in texts]

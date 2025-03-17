import operator
from typing import Annotated

from langchain_core.pydantic_v1 import BaseModel, Field

class State(BaseModel):
  query: str =  Field(
    ..., description='ユーザーからの質問'
  )
  current_role: str = Field(
    default='', description='選定された回答ロール'
  )
  messages: Annotated[list[str], operator.add] = Field(
    default=[], description='回答履歴'
  )
  current_judge: bool = Field(
    default=False, description='品質チェックの結果'
  )
  judgement_reason: str = Field(
    default='', description='品質チェックの判定理由'
  )

from langgraph.graph import StateGraph
from typing import Any

# ノード関数の実装
def answering_node(state: State) -> dict[str, Any]:
  query = state.query
  role = state.current_role

  # ユーザーからの質問内容と選択されたロールをもとに回答を生成するロジック
  generated_message = '' 
  return { "messages": [generated_message]}

workflow = StateGraph(State) # ステートグラフの初期化
workflow.add_node("answering",answering_node) # ノードの追加




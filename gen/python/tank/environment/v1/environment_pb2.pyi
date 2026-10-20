from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Metric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_UNSPECIFIED: _ClassVar[Metric]
    METRIC_MAE: _ClassVar[Metric]
    METRIC_BRIER: _ClassVar[Metric]
METRIC_UNSPECIFIED: Metric
METRIC_MAE: Metric
METRIC_BRIER: Metric

class Subject(_message.Message):
    __slots__ = ("id", "label")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class Score(_message.Message):
    __slots__ = ("product_workspace_id", "window_start", "window_end", "n", "value", "baseline_value", "skill", "provisional", "missed")
    PRODUCT_WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_START_FIELD_NUMBER: _ClassVar[int]
    WINDOW_END_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    PROVISIONAL_FIELD_NUMBER: _ClassVar[int]
    MISSED_FIELD_NUMBER: _ClassVar[int]
    product_workspace_id: str
    window_start: _timestamp_pb2.Timestamp
    window_end: _timestamp_pb2.Timestamp
    n: int
    value: float
    baseline_value: float
    skill: float
    provisional: bool
    missed: int
    def __init__(self, product_workspace_id: _Optional[str] = ..., window_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., window_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., n: _Optional[int] = ..., value: _Optional[float] = ..., baseline_value: _Optional[float] = ..., skill: _Optional[float] = ..., provisional: bool = ..., missed: _Optional[int] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ("workspace_id", "slug", "name", "slot", "url", "latest", "subscribed")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    LATEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    slug: str
    name: str
    slot: str
    url: str
    latest: Score
    subscribed: bool
    def __init__(self, workspace_id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., slot: _Optional[str] = ..., url: _Optional[str] = ..., latest: _Optional[_Union[Score, _Mapping]] = ..., subscribed: bool = ...) -> None: ...

class Environment(_message.Message):
    __slots__ = ("id", "slug", "name", "question", "source_name", "source_url", "horizon_minutes", "metric", "unit", "baseline", "subjects", "products", "observations", "predictions", "last_observed_at", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    HORIZON_MINUTES_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    BASELINE_FIELD_NUMBER: _ClassVar[int]
    SUBJECTS_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    OBSERVATIONS_FIELD_NUMBER: _ClassVar[int]
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    LAST_OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    slug: str
    name: str
    question: str
    source_name: str
    source_url: str
    horizon_minutes: int
    metric: Metric
    unit: str
    baseline: str
    subjects: _containers.RepeatedCompositeFieldContainer[Subject]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    observations: int
    predictions: int
    last_observed_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., question: _Optional[str] = ..., source_name: _Optional[str] = ..., source_url: _Optional[str] = ..., horizon_minutes: _Optional[int] = ..., metric: _Optional[_Union[Metric, str]] = ..., unit: _Optional[str] = ..., baseline: _Optional[str] = ..., subjects: _Optional[_Iterable[_Union[Subject, _Mapping]]] = ..., products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ..., observations: _Optional[int] = ..., predictions: _Optional[int] = ..., last_observed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Observation(_message.Message):
    __slots__ = ("subject", "at", "value")
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    subject: str
    at: _timestamp_pb2.Timestamp
    value: float
    def __init__(self, subject: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class Prediction(_message.Message):
    __slots__ = ("product_workspace_id", "subject", "made_at", "target_at", "value", "has_value", "baseline_value", "has_baseline", "status")
    PRODUCT_WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    MADE_AT_FIELD_NUMBER: _ClassVar[int]
    TARGET_AT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HAS_VALUE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_VALUE_FIELD_NUMBER: _ClassVar[int]
    HAS_BASELINE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    product_workspace_id: str
    subject: str
    made_at: _timestamp_pb2.Timestamp
    target_at: _timestamp_pb2.Timestamp
    value: float
    has_value: bool
    baseline_value: float
    has_baseline: bool
    status: str
    def __init__(self, product_workspace_id: _Optional[str] = ..., subject: _Optional[str] = ..., made_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ..., has_value: bool = ..., baseline_value: _Optional[float] = ..., has_baseline: bool = ..., status: _Optional[str] = ...) -> None: ...

class ArenaTurn(_message.Message):
    __slots__ = ("id", "round_id", "product_workspace_id", "product_name", "seq", "text", "at", "model")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROUND_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    round_id: str
    product_workspace_id: str
    product_name: str
    seq: int
    text: str
    at: _timestamp_pb2.Timestamp
    model: str
    def __init__(self, id: _Optional[str] = ..., round_id: _Optional[str] = ..., product_workspace_id: _Optional[str] = ..., product_name: _Optional[str] = ..., seq: _Optional[int] = ..., text: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., model: _Optional[str] = ...) -> None: ...

class Round(_message.Message):
    __slots__ = ("id", "window_end", "scoreboard", "scores", "turns", "opened_at", "comments")
    ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_END_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    window_end: _timestamp_pb2.Timestamp
    scoreboard: str
    scores: _containers.RepeatedCompositeFieldContainer[Score]
    turns: _containers.RepeatedCompositeFieldContainer[ArenaTurn]
    opened_at: _timestamp_pb2.Timestamp
    comments: int
    def __init__(self, id: _Optional[str] = ..., window_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., scoreboard: _Optional[str] = ..., scores: _Optional[_Iterable[_Union[Score, _Mapping]]] = ..., turns: _Optional[_Iterable[_Union[ArenaTurn, _Mapping]]] = ..., opened_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., comments: _Optional[int] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("id", "round_id", "name", "body", "at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROUND_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    round_id: str
    name: str
    body: str
    at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., round_id: _Optional[str] = ..., name: _Optional[str] = ..., body: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListEnvironmentsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEnvironmentsResponse(_message.Message):
    __slots__ = ("environments",)
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[Environment]
    def __init__(self, environments: _Optional[_Iterable[_Union[Environment, _Mapping]]] = ...) -> None: ...

class GetEnvironmentRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class GetEnvironmentResponse(_message.Message):
    __slots__ = ("environment",)
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    environment: Environment
    def __init__(self, environment: _Optional[_Union[Environment, _Mapping]] = ...) -> None: ...

class ListScoresRequest(_message.Message):
    __slots__ = ("environment_id", "product_workspace_id", "since", "limit")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    product_workspace_id: str
    since: _timestamp_pb2.Timestamp
    limit: int
    def __init__(self, environment_id: _Optional[str] = ..., product_workspace_id: _Optional[str] = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class ListScoresResponse(_message.Message):
    __slots__ = ("scores",)
    SCORES_FIELD_NUMBER: _ClassVar[int]
    scores: _containers.RepeatedCompositeFieldContainer[Score]
    def __init__(self, scores: _Optional[_Iterable[_Union[Score, _Mapping]]] = ...) -> None: ...

class ListObservationsRequest(_message.Message):
    __slots__ = ("environment_id", "subject", "since", "limit")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    subject: str
    since: _timestamp_pb2.Timestamp
    limit: int
    def __init__(self, environment_id: _Optional[str] = ..., subject: _Optional[str] = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class ListObservationsResponse(_message.Message):
    __slots__ = ("observations",)
    OBSERVATIONS_FIELD_NUMBER: _ClassVar[int]
    observations: _containers.RepeatedCompositeFieldContainer[Observation]
    def __init__(self, observations: _Optional[_Iterable[_Union[Observation, _Mapping]]] = ...) -> None: ...

class ListPredictionsRequest(_message.Message):
    __slots__ = ("environment_id", "product_workspace_id", "subject", "since", "limit", "upcoming")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    UPCOMING_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    product_workspace_id: str
    subject: str
    since: _timestamp_pb2.Timestamp
    limit: int
    upcoming: bool
    def __init__(self, environment_id: _Optional[str] = ..., product_workspace_id: _Optional[str] = ..., subject: _Optional[str] = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ..., upcoming: bool = ...) -> None: ...

class ListPredictionsResponse(_message.Message):
    __slots__ = ("predictions",)
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    predictions: _containers.RepeatedCompositeFieldContainer[Prediction]
    def __init__(self, predictions: _Optional[_Iterable[_Union[Prediction, _Mapping]]] = ...) -> None: ...

class ListRoundsRequest(_message.Message):
    __slots__ = ("environment_id", "cursor", "limit")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    cursor: str
    limit: int
    def __init__(self, environment_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListRoundsResponse(_message.Message):
    __slots__ = ("rounds", "next_cursor")
    ROUNDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    rounds: _containers.RepeatedCompositeFieldContainer[Round]
    next_cursor: str
    def __init__(self, rounds: _Optional[_Iterable[_Union[Round, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class ListCommentsRequest(_message.Message):
    __slots__ = ("environment_id", "round_id", "cursor", "limit")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ROUND_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    round_id: str
    cursor: str
    limit: int
    def __init__(self, environment_id: _Optional[str] = ..., round_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListCommentsResponse(_message.Message):
    __slots__ = ("comments", "next_cursor")
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[Comment]
    next_cursor: str
    def __init__(self, comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class PostCommentRequest(_message.Message):
    __slots__ = ("environment_id", "round_id", "name", "body", "consent", "website")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ROUND_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    round_id: str
    name: str
    body: str
    consent: bool
    website: str
    def __init__(self, environment_id: _Optional[str] = ..., round_id: _Optional[str] = ..., name: _Optional[str] = ..., body: _Optional[str] = ..., consent: bool = ..., website: _Optional[str] = ...) -> None: ...

class PostCommentResponse(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

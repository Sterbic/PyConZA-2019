blob = {
    "x": null,
    "numbers": [1, 2, 3],
    "object": {"y": 2}
}

JSONPrimitive = Union[int, float, str, None]
JSONList = List[JSONPrimiteve]
JSONObject = Dict[str, Union[JSONPrimitive, JSONList, "JSONObject"]]

JSON = Dict[str, Any]

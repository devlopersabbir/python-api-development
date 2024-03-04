## Declare Request Example Data

**We can define our example data with these types of way**

1. `Body()` normally `fastapi` body method

   - just use `examples` (**for list**) and `example` (**for a dict**)

2. `Field()` using pydantic field method
   - just use `example` as body method example
   ```py
   from pydantic import Field
   Field(examples=["Sabbir Hossain Shuvo"])
   ```
3. `model_config` pydantic attributes inside a model

   - for example

   ```py
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Fucker boy"
                }
            ]
        }
    }
   ```

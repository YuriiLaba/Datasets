from vega import VegaLite

VegaLite({
    "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
    "title": "Population of Ukraine 1989-2018",
    "data": {
        "url": "processed_population_by_age_sex_year.csv"
    },
    "vconcat": [
        {
            "width": 600,
            "height": 300,
            "mark": {
                "type": "line",
                "point": {
                    "filled": "false",
                    "fill": "white",
                    "strokeWidth": 2
                }
            },
            "selection": {
                "brush": {
                    "encodings": ["x"],
                    "type": "interval"
                }
            },
            "transform": [
                {
                    "filter": {
                        "selection": "click"
                    }
                },

                {
                    "calculate": "datum.sex == 2 ? 'Female' : 'Male'", "as": "gender"
                }
            ],
            "encoding": {
                "color": {
                    "field": "gender",
                    "type": "nominal",
                    "scale": {
                        "range": ["blue", "red"]
                    }
                },
                "x": {
                    "field": "year",
                    "type": "temporal",
                    "timeUnit": "year",
                    "sort": [],
                    "axis": {
                        "title": "date (only year)"
                    }
                },
                "y": {
                    "aggregate": "sum",
                    "field": "population",
                    "type": "quantitative",
                    "axis": {
                        "title": "population"
                    },
                    "scale": {
                        "domain": [5000000, 30000000]
                    }
                }
            }
        },
        {
            "mark": "bar",
            "selection": {
                "click": {
                    "encodings": ["color"],
                    "type": "multi"
                }
            },
            "transform": [
                {
                    "filter": {
                        "selection": "brush",
                    }
                },
                {
                    "calculate": "datum.sex == 2 ? 'Female' : 'Male'", "as": "gender"
                }
            ],
            "encoding": {
                "column": {
                    "field": "age",
                    "type": "ordinal",
                    "bin": {
                        "step": 5
                    },

                },
                "color": {
                    "field": "gender",
                    "type": "nominal",
                    "scale": {
                        "range": ["blue", "red"]
                    }
                },
                "x": {
                    "field": "gender",
                    "type": "nominal",
                    "scale": {
                        "rangeStep": 15
                    },
                    "axis": {
                        "title": ""
                    }
                },
                "y": {
                    "aggregate": "sum",
                    "field": "population",
                    "type": "quantitative",
                    "axis": {
                        "title": "population",
                        "grid": "false"
                    }
                },
                "opacity": {
                    "value": 0.7
                }
            }
        }
    ],
    "resolve": {
        "scale": {
            "color": "independent"
        }
    }
})

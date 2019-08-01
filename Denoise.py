    
    def MADFilter(self, num, name):
        codeStr = """{
        "pipeline":[
        "input.pcd",
        {
        "type":"filters.mad",
        "dimension": "axis", 
        "k":number
        },
        "output.pcd"
        ]
        }"""
        codeStr = codeStr.replace("input", name)
        codeStr = codeStr.replace("output", name)
        codeStr = codeStr.replace("number", num)
        #X axis
        codeStr = codeStr.replace("axis", "X")
        pipeline = pdal.Pipeline(codeStr)
        res = pipeline.execute()
        #Y axis
        codeStr = codeStr.replace("X", "Y")
        pipeline = pdal.Pipeline(codeStr)
        res = pipeline.execute()
        #Z axis
        codeStr = codeStr.replace("Y", "Z")
        pipeline = pdal.Pipeline(codeStr)
        res = pipeline.execute()
    

    def OutlierFilter(self, neighbor, thres):
        codeStr = """{
        "pipeline":[
        "input",
        {
        "type":"filters.outlier",
        "method":"statistical",
        "mean_k":neigh_n,
        "multiplier":threshold
        },
        {
        "type":"filters.range",
        "limits":"Classification![7:7]"
        },
        "output"
        ]
        }"""
        
        codeStr = codeStr.replace("input", file)
        
        codeStr = codeStr.replace("output", file)
        
        codeStr = codeStr.replace("neigh_n", str(neighbor))
        codeStr = codeStr.replace("threshold", str(thres))
        pipeline = pdal.Pipeline(codeStr)
        res = pipeline.execute()
        

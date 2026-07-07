from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from hashicorpvault.config.ConfigStore import *
from hashicorpvault.functions import *
from prophecy.utils import *
from hashicorpvault.graph import *

def pipeline(spark: SparkSession) -> None:
    df_tgt = tgt(spark)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("HashiCorpVault").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/HashiCorpVault")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/HashiCorpVault", config = Config)(pipeline)

if __name__ == "__main__":
    main()

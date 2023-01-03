from absl import app
from absl import flags
from parser import parser

FLAGS = flags.FLAGS
flags.DEFINE_string("url", None, "URL link of the online shopping website.")
flags.DEFINE_integer("max_collect", -1, "Maximum number of comments to collect. -1 if no limit.")
flags.DEFINE_boolean("collect_empty", True, "Collects empty comments if set to True")
flags.DEFINE_enum("browser", "Safari", ["Safari", "Firefox"], "Browser used for selenium. Can choose between Safari "
                                                              "and Firefox")

# Required flag.
flags.mark_flag_as_required("url")



def main(argv):
  parser(FLAGS)



if __name__ == '__main__':
  app.run(main)
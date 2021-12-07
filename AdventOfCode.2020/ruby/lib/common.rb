class Common
  def self.get_input(filename, delim = "\n")
    File.open(filename).read.split(delim)
  end
end

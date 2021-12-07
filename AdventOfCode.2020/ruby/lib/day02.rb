class Day02
  def self.do
    input = Common.get_input("inputs/day02")

    part1ValidCount = 0
    input.each do |line|
      parts = line.split(": ").map { |s| s.chomp }
      part1ValidCount += 1 if validate_part1(*parts)
    end
    puts "Part1 Valid Count: #{part1ValidCount}"

    part2ValidCount = 0
    input.each do |line|
      parts = line.split(": ").map { |s| s.chomp }
      part2ValidCount += 1 if validate_part2(*parts)
    end
    puts "Part2 Valid Count: #{part2ValidCount}"
  end

  def self.validate_part1(rule, input)
    if rule =~ /(\d+)-(\d+) (\w)/i
      count = input.count($3)
      return count >= $1.to_i && count <= $2.to_i
    end
    return false
  end

  def self.validate_part2(rule, input)
    if rule =~ /(\d+)-(\d+) (\w)/i
      index1 = $1.to_i - 1
      index2 = $2.to_i - 1
      return true if input[index1] == $3 && input[index2] != $3
      return true if input[index1] != $3 && input[index2] == $3
    end
    return false
  end
end

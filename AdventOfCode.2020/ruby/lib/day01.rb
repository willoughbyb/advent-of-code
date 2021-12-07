class Day01
  def self.do
    input = Common.get_input("inputs/day01").map { |i| i.to_i }
    input.each do |i|
      input.each do |j|
        input.each do |k|
          next if i == j || j == k

          if i + j + k == 2020
            p i * j * k
            return
          end
        end
      end
    end
  end
end

class Day03
  class Point
    attr_accessor :x, :y

    def initialize(x, y)
      @x = x
      @y = y
    end

    def +(other); Point.new(x + other.x, y + other.y); end
    def to_s; "(#{x},#{y})"; end
  end

  def self.do
    input = Common.get_input("inputs/day03")
    row_length = input[0].length
    slopes = [
      Point.new(1, 1),
      Point.new(3, 1),
      Point.new(5, 1),
      Point.new(7, 1),
      Point.new(1, 2),
    ]
    tree_counts = []

    slopes.each do |slope|
      tree_count = 0
      position = Point.new(0, 0)
      while position.y < input.length
        tree_count += 1 if input[position.y][position.x % row_length] == "#"
        position += slope
      end
      tree_counts << tree_count
    end

    puts "tree_counts: #{tree_counts}"
    puts tree_counts.reduce(1) { |c, a| a *= c }
  end

  private

  def self.puts_map(map)
    map.each do |line|
      puts line
    end
  end
end

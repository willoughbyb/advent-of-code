class Day04
  REQUIRED_FIELDS = %w(byr iyr eyr hgt hcl ecl pid)
  VALID_COLORS = %w(amb blu brn gry grn hzl oth)

  def self.do
    input = Common.get_input("inputs/day04", "\n\n").map { |line| line.split /\s/ }

    valid_count = 0
    input.each do |fields|
      is_valid = true
      REQUIRED_FIELDS.each do |required_field|
        field = get_required_field(fields, required_field)
        if field.nil?
          is_valid = false
          break
        end

        name, value = field.split(":")
        field_is_valid = case name
          when "byr"; value =~ /\d{4}/ && value.to_i >= 1920 && value.to_i <= 2002
          when "iyr"; value =~ /\d{4}/ && value.to_i >= 2010 && value.to_i <= 2020
          when "eyr"; value =~ /\d{4}/ && value.to_i >= 2020 && value.to_i <= 2030
          when "hgt"; value =~ /(\d+)(in|cm)/ && (($2 == "cm" && $1.to_i >= 150 && $1.to_i <= 193) ||
                                                  ($2 == "in" && $1.to_i >= 59 && $1.to_i <= 76))
          when "hcl"; value =~ /#[a-fA-F0-9]{6}/
          when "ecl"; VALID_COLORS.include? value
          when "pid"; value.length == 9
          else false
          end

        unless field_is_valid
          puts "Field is invalid: #{field}"
          is_valid = false
          break
        end
      end

      valid_count += 1 if is_valid
    end
    puts "valid count #{valid_count}"
  end

  private

  def self.get_required_field(fields, fieldName)
    fields.each do |field|
      return field if field.start_with? fieldName
    end
    nil
  end
end

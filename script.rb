#for loading csv file
ratio = []
File.readlines('ratio.txt').map do |line|
  ratio << line.strip
end
companies_name = []
data = CSV.read("company_data.csv", headers: true)
data.each do |item|
	companies_name << item[0]
end
final_strings = []
companies_name.each do |com|
	ratio.each do |item|
	  string = com + " " + item
	  final_strings << string
	  string = item + " " + com
	  final_strings << string
	end
end
File.open("whitelabelled_words.txt", "w+") do |f|
  final_strings.each { |element| f.puts(element) }
end
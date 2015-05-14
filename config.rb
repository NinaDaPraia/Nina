require "pacto"

Pacto.configure do |c|
  c.contracts_path = "contracts"
  c.strict_matchers = true

  c.register_hook do |contracts, request, response|
    puts "Received #{request}"
  end
end
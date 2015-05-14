require "pacto"
require 'pacto/rspec'

Pacto.configure do |c|
  c.contracts_path = "contracts"
end

API_HOST = ENV.fetch('API_HOST', 'http://localhost:8000')

pacto_mode = ENV['PACTO_MODE']
require "pacto_modes/#{pacto_mode}" if pacto_mode

stub_provider = ENV['STUB_WITH']
if stub_provider
  puts "Stubbing with: #{stub_provider}"
  require "stub_providers/#{stub_provider}"
else
  puts "Running live tests"
  WebMock.allow_net_connect!
end
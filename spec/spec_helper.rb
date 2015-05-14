require "pacto"
require 'pacto/rspec'

Pacto.configure do |c|
  c.contracts_path = "contracts"
end

API_HOST = ENV.fetch('API_HOST', 'http://localhost:8000')

pacto_mode = ENV['PACTO_MODE']
require "pacto_modes/#{pacto_mode}" if pacto_mode

WebMock.allow_net_connect!
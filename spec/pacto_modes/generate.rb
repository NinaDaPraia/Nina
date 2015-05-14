Pacto::Generator.configure do |c|
  c.hint 'API root endpoint', http_method: :get, host: 'http://localhost:8000', path: '/'
end

Pacto.generate!
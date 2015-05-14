Pacto::Generator.configure do |c|
  c.hint 'API root endpoint', http_method: :get, host: API_HOST, path: '/'
end

Pacto.generate!
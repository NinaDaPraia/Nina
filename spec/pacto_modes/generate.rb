Pacto::Generator.configure do |c|
  c.hint 'API root endpoint', http_method: :get, host: 'http://nina-staging.herokuapp.com', path: '/'
end

Pacto.generate!